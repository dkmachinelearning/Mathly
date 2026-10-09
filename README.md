# 🧮 Mathly - Moja przygoda z matematyką

**Mathly** to interaktywna aplikacja webowa stworzona w Pythonie przy użyciu biblioteki **Streamlit**. Aplikacja powstała z myślą o dzieciach uczących się matematyki oraz ich rodzicach, którzy chcą w prosty sposób kontrolować zakres i poziom trudności zadań.

Aplikacja doskonale działa zarówno na komputerach, jak i urządzeniach mobilnych (tabletach oraz smartfonach).

---

## ✨ Funkcje aplikacji

### ⚙️ Panel Rodzica (Boczny pasek)
*   **Pełna kontrola zakresu:** Możliwość ustawienia minimalnej i maksymalnej wartości liczb (aż do 1000) za pomocą suwaka.
*   **Wybór długości serii:** Rodzic decyduje, z ilu zadań ma składać się dany test (np. 10, 20 pytań).
*   **Wybór operacji:** Dowolne miksowanie typów działań – od podstawowych po zaawansowane.

### 🎮 Panel Dziecka (Główny ekran)
*   **Siedem trybów gry:** Dodawanie, odejmowanie, mnożenie, dzielenie, potęgowanie (A² lub A³), dzielenie z resztą oraz pierwiastkowanie (\(\sqrt{A}\)).
*   **Pedagogiczne podejście (Dwie próby):** Jeśli dziecko się pomyli, aplikacja nie pokazuje od razu wyniku, lecz motywuje komunikatem: *"To zły wynik, ale spróbuj jeszcze raz!"* i pozwala poprawić błąd.
*   **Inteligentne generowanie zadań:** 
    *   Brak wyników ujemnych przy odejmowaniu.
    *   Zawsze ładne wyniki całkowite przy dzieleniu i pierwiastkowaniu.
    *   Automatyczne dopasowanie trudności dzielenia i mnożenia (w pamięci, bez wielkich liczb), nawet gdy ogólny zakres ustawiony jest do 1000.
*   **Ekran podsumowania:** Po zakończeniu serii system odpala wirtualne balony, wystawia ocenę gwiazdkową i wyświetla rodzicowi listę przykładów, które sprawiły dziecku trudność.

---

## 🛠️ Jak uruchomić aplikację lokalnie?

Jeśli chcesz odpalić aplikację na swoim komputerze, upewnij się, że masz zainstalowanego Pythona, a następnie:

1.  **Sklonuj to repozytorium** lub pobierz pliki na dysk.
2.  **Zainstaluj wymagane biblioteki** za pomocą terminala:
    ```bash
    pip install streamlit
    ```
3.  **Uruchom serwer Streamlit**:
    ```bash
    streamlit run app.py
    ```
4.  Aplikacja automatycznie otworzy się w Twojej przeglądarce internetowej pod adresem `http://localhost:8501`.

---

## ☁️ Publikacja w Streamlit Cloud

Projekt jest w pełni kompatybilny z darmowym hostingiem **Streamlit Cloud**. Aby udostępnić aplikację dziecku online:
1. Wrzuć pliki `app.py` oraz `requirements.txt` do tego repozytorium na GitHubie.
2. Zaloguj się na [share.streamlit.io](https://streamlit.io) poprzez konto GitHub.
3. Wskaż to repozytorium i kliknij **Deploy**.

---
*Projekt stworzony z myślą o mądrej i bezstresowej edukacji najmłodszych! 🚀*
