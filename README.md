# Лабораторна робота №3. Лозко Олександр.

Сайт: https://lozkolab3.herokuapp.com/index
Бренди одягу та їх продукція.

Існує дві таблиці: 
- Бренд: Назва(PK), Рік заснування.
- Продукція: ID(PK), Назва, Ціна, Бренд(FK).

Щоб розгорнути локально:
1. Скачати репозиторій.
2. Встановити requirements.txt.
3. Замінити в app.config['SQLALCHEMY_DATABASE_URI'] на 'postgresql://*ім'я користувача*:*пароль*@localhost:*порт*/*назва БД*'.
4. Запустити app.py.

Щоб розгорнути на Heroku:
1. Завантажити до себе цей репозиторій.
2. Підключити GitHub до Heroku.
3. Задеплоїти.

ERD:
![Image alt](https://github.com/aleksandrlozko/lab_3/blob/9f504135db24123e659eb86ceaf7a94df3859d0e/ERD.png)
