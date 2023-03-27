"""
Задача 1.
Даны две даты в виде строк формата YYYY-MM-DD. Посчитать количество дней между
этими датами без использования библиотек.
Примеры:
Дано: date1 = "2019-06-29", date2 = "2019-06-30"
Результат: 1
Дано: date1 = "2020-01-15", date2 = "2019-12-31"
Результат: 15
"""

date1 = "2019-06-29"
date2 = "2019-06-30"

def day(date: str):

    splitDate = date.split('-')
    year = int(splitDate[0])-1
    month = int(splitDate[1])
    day = int(splitDate[2])

    isLeapYear = year % 4 == 0
    february = 29 if isLeapYear else 28

    monthArr = [31,february,31,30,31,30,31,31,30,31,30,31]
    leapDaysInYear = year // 4
    daysInYears = (leapDaysInYear * 366 + ((year - leapDaysInYear) * 365))

    daysInMonth =  sum(monthArr[:month -1:])
    result = daysInYears + daysInMonth + day
    return result

result = day(date1) - day(date2)
print(abs(result))
