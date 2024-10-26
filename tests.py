import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len (collector.get_books_genre()) == 2
    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    #Проверка установления жанра по умолчанию в добавленнй книге
    def test_add_new_book_chack_genre(self,collection):
        first_book = 'Новая книга'
        collection.add_new_book(first_book)
        assert collection.get_book_genre(first_book) == ''

    #некативная проверка на добавление книг с именем 0 и более 41 символа
    @pytest.mark.parametrize('book',[''*41])
    def test_add_new_book_add_long_name(self,book,collection):
        collection.add_new_book(book)
        assert len (collection.get_books_genre()) == 0

    #Негативная проверка повторного добавления одинакоковых книг
    def Test_add_new_book_double_not_added(self,collection):
        books = ['Книга','Книга']
        for book in books:
            collection.add_new_book(book)
        assert len(collection.get_books_genre()) == 1

    #Проверка добавления жанра из списка genre из списка books_genre
    def test_set_book_genre_added(self,collection):
        first_book = 'Книга 2'
        genre = 'Фантастика'
        collection.add_new_book(first_book)
        collection.set_book_genre(first_book,genre)
        assert collection.get_book_genre(first_book) == genre

    #Проверка изменения жанра из списка genre из книги books_genre
    def test_set_book_genre_change(self, collection):
        first_book = 'Книга 3'
        genre = 'Ужасы'
        other_genre = 'Комедии'
        collection.add_new_book(first_book)
        collection.set_book_genre(first_book,genre)
        collection.set_book_genre(first_book,other_genre)
        assert collection.get_book_genre(first_book) == other_genre

    #Негативная проверка добавления жанра не из списка genre из списка books_genre
    def test_set_book_genre_miss_genre_not_add(self, collection):
        first_book = 'Новая книга 2'
        missing_genre = 'Приключение'
        collection.add_new_book(first_book)
        collection.set_book_genre(first_book,missing_genre)
        assert collection.get_book_genre(first_book) == ''

    #Проверка вывода книг определенного жанра
    def test_get_books_specific_genre_succ(self, collection_five_books):
        assert collection_five_books.get_books_specific_genre('Ужасы') == ['Зеркало']

    #Негативная проверка вывода отсутсвующей книги определенного жанра
    def test_get_books_specific_genre_missing_book(self,collection_five_books):
        assert len (collection_five_books.get_books_specific_genre('Приключения'))==0

    #Проверка вывода списка книг с жанром для детей
    def test_get_book_for_children(self,collection_five_books):
        chilsren_books = collection_five_books.get_books_for_children()
        assert len(chilsren_books) == 3 and chilsren_books == ['Книга 1','Книга 2']

    #Проверка добавления книги из списка books_genre в избранное
    def test_add_book_in_favorit(self,collection):
        first_book = 'Книга 1'
        collection.add_new_book(first_book)
        collection.add_book_in_favorites(first_book)
        favorites = collection.get_list_of_favorites_books()
        assert len(favorites) == 1 and favorites[0] == first_book

    #Негативная проверка добавления книг не из списка books_genre  в избранное
    def test_add_book_in_favorite_and_miss_book(self,collection):
        first_book = 'Книга 2'
        collection.add_book_in_favorites(first_book)
        assert len =(collection.get_list_of_favorites_books()) == 0

    #Негативная проверка повторного добавления книги в избранное
    def test_add_book_in_favorites_add_double_books_not_added(self,collection):
        first_book = 'Книга 2'
        collection.add_new_book(first_book)
        collection.add_book_in_favorites(first_book)
        collection.add_book_in_favorites(first_book)
        favorites = collection.get_list_of_favorites_books()
        assert len(favorites) == 1 and favorites[0] == first_book

    #Проверка удаления книги из списка избранного
    def test_delete_book_from_favorites_book_deleted(self,collection):
        first_book = 'Книга 2'
        collection.add_new_book(first_book)
        collection.add_book_in_favorites(first_book)
        collection.delete_book_from_favorites(first_book)
        assert len (collection.get_list_of_favorites_books()) == 0

    #Негативная проверка удаление не добавленной книги в favorites
    def test_delete_book_from_favorites_miss_book_not_deleted(self,collection):
        first_book = 'Книга 3'
        second_book = 'Книга 2'
        collection.add_new_book(first_book)
        collection.add_book_in_favorites(first_book)
        collection.delete_book_from_favorites(second_book)
        favorites = collection.get_list_of_favorites_books()
        assert len(favorites) == 1 and favorites[0] == first_book