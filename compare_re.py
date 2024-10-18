import exrex
import re

a = r'a*b*|a(a|b)*|bb' # Введите свое регулярное выражение
b = r'a(a|b)*|bb|1' # Введите регулярное выражение для сравнения


def main():
    i = 0
    for test in exrex.generate(b, 110):
        if re.match(a, test) is None:
            print(test)
            print('Not matched')
            return
        i += 1
        if i == 1000000:
            print('All gut')
            return
    print(i)



if __name__ == '__main__':
    main()