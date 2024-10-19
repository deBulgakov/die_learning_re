import exrex
import re
import math

a = r'a*b*|a(a|b)*|bb'  # Введите свое регулярное выражение
b = r'a(a|b)*|bb|1'  # Введите регулярное выражение для сравнения
alph = 'abcdef'

def main():
    i = 0
    n_used = len(set([i for i in alph if i in a or i in b]))
    limit_tests = 100 ** (max(a.count('|'), b.count('|'), n_used))
    limit_generated = math.ceil(math.log(limit_tests, n_used))
    for test in exrex.generate(b, limit_generated):
        if re.match(a, test) is None:
            print(test)
            print('Not matched')
            return
        i += 1
        if i == limit_tests:
            print('All gut')
            return
    print(i)


if __name__ == '__main__':
    main()
