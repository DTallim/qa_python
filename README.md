# qa_python
Файлы
conftest.py - вспомогательные функции фикстуры
main.py - класс BookCollector

test_main.py: тестовый класс TestBookCollector
test_add_new_book_add_two_bookse: Проверка добавления двух книг в словарь books_genre
test_add_new_book_chack_genre: роверка установления жанра по умолчанию в добавленнй книге
test_add_new_book_add_long_name:екативная проверка на добавление книг с именем 0 и более 41 символа
Test_add_new_book_double_not_added:Негативная проверка повторного добавления одинакоковых книг
test_set_book_genre_added: роверка добавления жанра из списка genre из списка books_genre
test_set_book_genre_change: Проверка изменения жанра из списка genre из книги books_genre
test_set_book_genre_miss_genre_not_add: Негативная проверка добавления жанра не из списка genre из списка books_genre
test_get_books_specific_genre_succ: Проверка вывода книг определенного жанра
test_get_books_specific_genre_missing_book: Негативная проверка вывода отсутсвующей книги определенного жанра
test_get_book_for_children: Проверка вывода списка книг с жанром для детей
test_add_book_in_favorit: роверка добавления книги из списка books_genre в избранное
est_add_book_in_favorite_and_miss_book: Негативная проверка добавления книг не из списка books_genre  в избранное
test_add_book_in_favorites_add_double_books_not_added: Негативная проверка повторного добавления книги в избранное
test_delete_book_from_favorites_book_deleted: Проверка удаления книги из списка избранного
test_delete_book_from_favorites_miss_book_not_deleted: Негативная проверка удаление не добавленной книги в favorites



Команда для запуска теста: pytest -v

Команда для оценки покрытия: pytest --cov=main

Результат выполнения тестов:
Результат оценки покрытия с учетом ветвления: