from math import sqrt


# 1
def arithmetic(a, b, operation):
    if operation == '+':
        return a + b

    if operation == '-':
        return a - b

    if operation == '*':
        return a * b

    if operation == '/':
        return a / b

# 2
def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False

# 3
def square(a):
    p = 4 * a
    s = a * a
    d = sqrt(2) * a

    return [p, s, d]

# 4
def season(month):
    if month >= 1 and month <= 3:
        return "Talv"

    if month >= 4 and month <= 6:
        return "Kevad"

    if month >= 7 and month <= 9:
        return "Suvi"

    if month >= 10 and month <= 12:
        return "Sugis"

# 5
def bank(a, years):
    s = a * (1 + 0.1) ** years
    return s

# 6
# https://pythonist.ru/proverka-chisla-na-prostotu/
def is_prime(a):
    if a < 0 or a > 1000:
        return
    k = 0
    for i in range(2, a // 2+1):
        if (a % i == 0):
            k = k+1
    if (k <= 0):
        return True
    else:
        return False

# 7
def date(day, month, year):
   if day <= 0 or month <= 0 or year < 0:
       return False
   else:
       months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
       if year % 4 == 0:  months[1] = 29
       if day <= months[month - 1]:
           if month <= 12:
               return True
       return False