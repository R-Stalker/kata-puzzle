# -*- coding:utf-8 -*-
def fizz_buzz(n, n1, n2):
    result_list = list()
    for x in range(1, n + 1):
        if str(n1) in str(x) and str(n2) in str(x):
            result_list.append("FizzBuzz")
        elif x % n1 == 0:
            if x % n2 == 0:
                result_list.append("FizzBuzz")
            else:
                result_list.append("Fizz")
        elif x % n2 == 0:
            result_list.append("Buzz")
        elif str(n1) in str(x):
            result_list.append("Fizz")
        elif str(n2) in str(x):
            result_list.append("Buzz")
        else:
            result_list.append(x)
    for value in result_list:
        print(value)
    return result_list


if __name__ == "__main__":
    input_n = 100
    num1 = 3
    num2 = 5
    fizz_buzz(input_n, num1, num2)
