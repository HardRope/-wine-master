# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

- Скачайте код
- Откройте консоль и перейдите в каталог со скачанным кодом
- Установите зависимости 

``` 
pip install -r requirements.txt
```

- Создайте файл `.env` и добавьте в него переменную `WINES`, где `file` - название файла
с данными о винах или путь, если файл лежит не в директории с кодом

```
WINES='file.xlsx'
```

- Запустите сайт командой 

```
python3 main.py
```

- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

Для корректной работы кода требуется файл `wines_catalogue.xlsx`, содержащий таблицу с
информацией о винах в виде:

Категория	|Название	| Сорт	         |Цена	|Картинка	        |Акция               |
------------|-----------|---------------|-------|-------------------|--------------------|
Белые вина	|Белая леди	| Дамский пальчик |399	|belaya_ledi.png	|Выгодное предложение|
Красные вина|Черный лекарь|Качич	  |399	|chernyi_lekar.png	| |


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
