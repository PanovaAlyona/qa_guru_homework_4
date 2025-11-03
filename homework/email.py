import datetime
import json

# 1. Создаем словарь email
email = {
    "subject": "Quarterly Report",
    "from": "  Alice.Cooper@Company.ru ",
    "to": "   bob_smith@Gmail.com   ",
    "body": "Hello Bob,\n\tHere is the quarterly report.\n\tPlease review and let me know your feedback.\n\nBest,"
    "\nAlice",
}

# 2. Добавить дату отправки:
send_date = datetime.datetime.now().strftime("%Y-%m-%d")
email["date"] = send_date

# 3. Нормализовать e-mail адреса отправителя и получателя: приведите к нижнему регистру и уберите пробелы по краям.
email["from"] = email["from"].lower().strip()
email["to"] = email["to"].lower().strip()

# 4. Извлечь логин и домен отправителя в две переменные login и domain.
login, domain = email["from"].split("@")

# 5. Создайте сокращённую версию текста: возьмите первые 10 символов email["body"] и добавьте многоточие "...".
#   Сохраните в новый ключ словаря: email["short_body"].
email["short_body"] = email["body"][:10] + "..."

# 6. Списки доменов: создайте список личных доменов
personal_domains = [
    "gmail.com",
    "list.ru",
    "yahoo.com",
    "outlook.com",
    "hotmail.com",
    "icloud.com",
    "yandex.ru",
    "mail.ru",
    "list.ru",
    "bk.ru",
    "inbox.ru",
]
unique_personal_domains = list(set(personal_domains))

corporate_domains = [
    "company.ru",
    "corporation.com",
    "university.edu",
    "organization.org",
    "company.ru",
    "business.net",
]
unique_corporate_domains = list(set(corporate_domains))

# 7. Проверьте что в списке личных и корпоративных доменов нет пересечений: ни один домен не должен входить в оба
#   списка одновременно.
has_intersection = any(
    item in unique_personal_domains for item in unique_corporate_domains
)

# 8. Проверьте «корпоративность» отправителя: создайте булеву переменную is_corporate, равную результату проверки
#   вхождения домена отправителя в список корпоративных доменов.
is_corporate = domain in unique_corporate_domains

# 9. Соберите «чистый» текст сообщения без табов и переводов строк: замените "\t" и "\n" на пробел.
#   Сохраните в email["clean_body"].
email["clean_body"] = email["body"].replace("\t", " ").replace("\n", " ")

# 10. Сформируйте текст отправленного письма многострочной f-строкой и сохраните в email["sent_text"]:
#    Кому: {получатель}, от {отправитель} Тема: {тема письма}, дата {дата} {чистый текст сообщения}
email["sent_text"] = (
    f"Кому: {email['to']},\nот: {email['from']}\nТема: {email['subject']},\nдата: {email['date']}\n"
    + f"{email['clean_body']}"
)

# 11. Рассчитайте количество страниц печати для email["sent_text"], если на 1 страницу помещается 500 символов.
#    Сохраните результат в переменную pages. Значение должно быть округленно в большую сторону
pages = (len(email["sent_text"]) + 499) // 500

# 12. Проверьте пустоту темы и тела письма: создайте переменные is_subject_empty, is_body_empty
#    в котором будет хранится что тема письма содержит данные
is_subject_empty = email["subject"] == ""
is_body_empty = email["body"] == ""

# 13. Создайте «маску» e-mail отправителя: первые 2 символа логина + "***@" + домен.
#    Запишите в email["masked_from"].
email["masked_from"] = login[:2] + "***@" + domain

# 14. Удалите из списка личных доменов значения "list.ru" и "bk.ru".
unique_personal_domains.remove("list.ru")
unique_personal_domains.remove("bk.ru")


print(f"Словарь email:\n", json.dumps(email, indent=4, ensure_ascii=False))

print(
    f"Список уникальных личных доменов: {unique_personal_domains}",
    f"Список уникальных корпоративных доменов: {unique_corporate_domains}",
    f"Проверка пересечения списков доменов: {has_intersection}",
    f"Проверка корпоративности отправителя: {is_corporate}",
    f"Количество страниц печати для sent_text: {pages}",
    f"Проверка пустоты темы письма: {is_subject_empty}",
    f"Проверка пустоты тела письма: {is_body_empty}",
    sep="\n",
)
