#writefile app.py
import streamlit as st
import random
import math

# --- KONFIGURACJA STRONY ---
st.set_page_config(page_title="Matematyka dla Dzieci", page_icon="🧮", layout="centered")
st.title("🧮 Mathly - Moja przygoda z matematyką")

# --- INICJALIZACJA STANU APLIKACJI ---
if "liczba1" not in st.session_state:
    st.session_state.liczba1 = 0
    st.session_state.liczba2 = 0
    st.session_state.dzialanie = "+"
    st.session_state.poprawny_wynik = 0
    st.session_state.poprawna_reszta = 0  
    st.session_state.wylosowano = False
    st.session_state.punkty = 0
    st.session_state.odpowiedziano = False
    st.session_state.aktualne_zadanie = 1
    st.session_state.historia_bledow = []
    st.session_state.koniec_serii = False
    st.session_state.proba = 1

# --- PANEL RODZICA (Boczny pasek) ---
st.sidebar.header("⚙️ Ustawienia dla działań")
min_zakres, max_zakres = st.sidebar.slider(
    "Wybierz zakres liczb (dla +/-):", 
    min_value=1, max_value=1000, value=(1, 100)
)
ilosc_zadan = st.sidebar.number_input(
    "Ilość zadań w serii:",
    min_value=1, max_value=50, value=10, step=1
)
operacje = st.sidebar.multiselect(
    "Dozwolone działania:",
    [
        "Dodawanie (+)", "Odejmowanie (-)", "Mnożenie (×)", 
        "Dzielenie (÷)", "Potęgowanie (A²)", "Dzielenie z resztą (R)", "Pierwiastkowanie (√)"
    ],
    default=["Dodawanie (+)"]
)

def resetuj_gre():
    st.session_state.punkty = 0
    st.session_state.aktualne_zadanie = 1
    st.session_state.historia_bledow = []
    st.session_state.koniec_serii = False
    st.session_state.wylosowano = False
    st.session_state.odpowiedziano = False
    st.session_state.proba = 1

if st.sidebar.button("Resetuj i zacznij od nowa 🔄"):
    resetuj_gre()
    st.rerun()

# --- LOGIKA LOSOWANIA ZADANIA ---
def losuj_zadanie():
    if not operacje:
        st.warning("Rodzicu, wybierz przynajmniej jedno działanie w panelu bocznym!")
        return

    wybrane_dzialanie = random.choice(operacje)
    st.session_state.poprawna_reszta = 0  
    
    if "Dodawanie" in wybrane_dzialanie:
        st.session_state.liczba1 = random.randint(min_zakres, max_zakres)
        st.session_state.liczba2 = random.randint(min_zakres, max_zakres)
        st.session_state.dzialanie = "+"
        st.session_state.poprawny_wynik = st.session_state.liczba1 + st.session_state.liczba2
        
    elif "Odejmowanie" in wybrane_dzialanie:
        l1 = random.randint(min_zakres, max_zakres)
        l2 = random.randint(min_zakres, max_zakres)
        st.session_state.liczba1 = max(l1, l2)
        st.session_state.liczba2 = min(l1, l2)
        st.session_state.dzialanie = "-"
        st.session_state.poprawny_wynik = st.session_state.liczba1 - st.session_state.liczba2
        
    elif "Mnożenie" in wybrane_dzialanie:
        st.session_state.liczba1 = random.randint(min_zakres, min(max_zakres, 100))
        st.session_state.liczba2 = random.randint(1, 10)
        st.session_state.dzialanie = "×"
        st.session_state.poprawny_wynik = st.session_state.liczba1 * st.session_state.liczba2
        
    elif "Dzielenie" in wybrane_dzialanie:
        maks_wynik = 30 if max_zakres > 100 else 12
        poprawny = random.randint(2, maks_wynik)
        st.session_state.liczba2 = random.randint(2, 10)
        st.session_state.liczba1 = poprawny * st.session_state.liczba2
        st.session_state.dzialanie = "÷"
        st.session_state.poprawny_wynik = poprawny

    elif "Potęgowanie" in wybrane_dzialanie:
        st.session_state.liczba2 = random.choice([2, 3])
        if st.session_state.liczba2 == 3:
            st.session_state.liczba1 = random.randint(1, min(max_zakres, 10)) 
        else:
            st.session_state.liczba1 = random.randint(1, min(max_zakres, 31))
        st.session_state.dzialanie = "^"
        st.session_state.poprawny_wynik = st.session_state.liczba1 ** st.session_state.liczba2

    elif "Dzielenie z resztą" in wybrane_dzialanie:
        maks_dzielna = min(max_zakres, 150)
        st.session_state.liczba1 = random.randint(10, maks_dzielna)
        st.session_state.liczba2 = random.randint(3, 10)
        st.session_state.dzialanie = "÷ z resztą"
        st.session_state.poprawny_wynik = st.session_state.liczba1 // st.session_state.liczba2
        st.session_state.poprawna_reszta = st.session_state.liczba1 % st.session_state.liczba2

    elif "Pierwiastkowanie" in wybrane_dzialanie:
        baza = random.randint(1, min(max_zakres, 31))
        st.session_state.liczba1 = baza ** 2
        st.session_state.dzialanie = "√"
        st.session_state.poprawny_wynik = baza

    st.session_state.wylosowano = True
    st.session_state.odpowiedziano = False
    st.session_state.proba = 1  

# Losuj pierwsze zadanie przy uruchomieniu
if not st.session_state.wylosowano and not st.session_state.koniec_serii:
    losuj_zadanie()

# --- PANEL DZIECKA ---
if st.session_state.koniec_serii:
    st.balloons()
    st.success("## 🎉 Gratulacje! Ukończyłeś całą serię zadań!")
    st.markdown(f"### 🏆 Twój wynik końcowy to: **{st.session_state.punkty} z {ilosc_zadan} punktów**")
    
    procent = (st.session_state.punkty / ilosc_zadan) * 100
    if procent == 100:
        st.markdown("### 👑 Mistrz Matematyki! Perfekcyjny wynik! ⭐⭐⭐")
    elif procent >= 80:
        st.markdown("### 🌟 Wspaniale Ci poszło! Jesteś super! ⭐⭐")
    elif procent >= 50:
        st.markdown("### 👍 Dobra robota! Ćwiczenie czyni mistrza! ⭐")
    else:
        st.markdown("### 💪 Nie poddawaj się! Następnym razem pójdzie lepiej!")

    if st.session_state.historia_bledow:
        st.write("---")
        st.markdown("#### 📝 Zobacz, które przykłady warto jeszcze potrenować:")
        for blad in st.session_state.historia_bledow:
            st.warning(blad)
            
    if st.button("Zagraj jeszcze raz 🎮"):
        resetuj_gre()
        st.rerun()

else:
    st.markdown(f"#### 📊 Zadanie {st.session_state.aktualne_zadanie} z {ilosc_zadan}")
    st.subheader(f"⭐ Twoje punkty: {st.session_state.punkty}")
    st.markdown(f"## Ile to jest?")

    if st.session_state.dzialanie == "^":
        st.markdown(f"# {st.session_state.liczba1}<sup>{st.session_state.liczba2}</sup> = ?", unsafe_allow_html=True)
    elif st.session_state.dzialanie == "√":
        st.markdown(f"# √{st.session_state.liczba1} = ?")
    else:
        st.markdown(f"# {st.session_state.liczba1} {st.session_state.dzialanie} {st.session_state.liczba2} = ?")

    # Formularz na odpowiedź
    with st.form(key='matma_form', clear_on_submit=False):
        if st.session_state.dzialanie == "÷ z resztą":
            col1, col2 = st.columns(2)
            with col1:
                user_input = st.number_input("Wynik całkowity:", step=1, value=None, placeholder="Wynik...")
            with col2:
                user_reszta = st.number_input("Reszta:", step=1, value=None, placeholder="Reszta...")
        else:
            user_input = st.number_input("Wpisz wynik i kliknij Sprawdź:", step=1, value=None, placeholder="Twój wynik...")
            user_reszta = 0  

        submit_button = st.form_submit_button(label='Sprawdź! 🚀', disabled=st.session_state.odpowiedziano)

    # Sprawdzanie odpowiedzi
    if submit_button:
        czy_wypelniono = (user_input is not None and user_reszta is not None) if st.session_state.dzialanie == "÷ z resztą" else (user_input is not None)
        
        if czy_wypelniono:
            if st.session_state.dzialanie == "÷ z resztą":
                poprawnie = (user_input == st.session_state.poprawny_wynik) and (user_reszta == st.session_state.poprawna_reszta)
                tekst_dzialania = f"{st.session_state.liczba1} ÷ {st.session_state.liczba2} = {st.session_state.poprawny_wynik} r. {st.session_state.poprawna_reszta}"
                komunikat_finalny = f"😢 Blisko! Wynik to {st.session_state.poprawny_wynik} i reszty {st.session_state.poprawna_reszta}"
            else:
                poprawnie = (user_input == st.session_state.poprawny_wynik)
                if st.session_state.dzialanie == "^":
                    tekst_dzialania = f"{st.session_state.liczba1}^{st.session_state.liczba2} = {st.session_state.poprawny_wynik}"
                elif st.session_state.dzialanie == "√":
                    tekst_dzialania = f"√{st.session_state.liczba1} = {st.session_state.poprawny_wynik}"
                else:
                    tekst_dzialania = f"{st.session_state.liczba1} {st.session_state.dzialanie} {st.session_state.liczba2} = {st.session_state.poprawny_wynik}"
                komunikat_finalny = f"😢 Blisko! Prawidłowy wynik to: {st.session_state.poprawny_wynik}"

            if poprawnie:
                st.success("🎉 Super! Doskonała odpowiedź! 🌟")
                st.session_state.punkty += 1
                st.session_state.odpowiedziano = True
            else:
                if st.session_state.proba == 1:
                    st.warning("⚠️ To zły wynik, ale spróbuj jeszcze raz! Możesz poprawić liczbę powyżej. 💪")
                    st.session_state.proba = 2
                else:
                    st.error(komunikat_finalny)
                    wpis_bledu = f"❌ {tekst_dzialania} (Twoja odpowiedź: {user_input}" + (f" r. {user_reszta})" if st.session_state.dzialanie == "÷ z resztą" else ")")
                    st.session_state.historia_bledow.append(wpis_bledu)
                    st.session_state.odpowiedziano = True
        else:
            st.info("Wpisz odpowiedź przed sprawdzeniem!")

    # Przycisk przejścia dalej
    if st.session_state.odpowiedziano:
        napis_przycisku = "Zobacz wyniki 🏁" if st.session_state.aktualne_zadanie >= ilosc_zadan else "Następne pytanie ➡️"
        
        if st.button(napis_przycisku):
            if st.session_state.aktualne_zadanie >= ilosc_zadan:
                st.session_state.koniec_serii = True
            else:
                st.session_state.aktualne_zadanie += 1
                losuj_zadanie()
            st.rerun()
