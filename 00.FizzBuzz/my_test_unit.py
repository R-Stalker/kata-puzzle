# -*- coding: utf-8 -*-

import unittest
import fizzbuzz


class MyTestFunc(unittest.TestCase):
    def test_3_5(self):
        result_list = fizzbuzz.fizz_buzz(100, 3, 5)
        for i in range(1, 101):
            if i == 35 or i == 53:
                self.assertEqual("FizzBuzz", result_list[i - 1])  # 同时包含3和5应喊FizzBuzz
            elif i % 3 == 0:
                if i % 5 == 0:
                    self.assertEqual("FizzBuzz", result_list[i - 1])  # 同时为3和5的倍数应喊FizzBuzz
                else:
                    self.assertEqual("Fizz", result_list[i - 1])  # 仅为3的倍数应喊Fizz
            elif i % 5 == 0:
                self.assertEqual("Buzz", result_list[i - 1])  # 仅为5的倍数应喊Buzz
            elif '3' in str(i):
                self.assertEqual("Fizz", result_list[i - 1])  # 仅包含3应喊Fizz
            elif '5' in str(i):
                self.assertEqual("Buzz", result_list[i - 1])  # 仅包含5应喊Buzz
            else:
                self.assertEqual(i, result_list[i - 1])  # 其余情况喊原来的数字

    def test_2_7(self):
        result_list = fizzbuzz.fizz_buzz(100, 2, 7)
        for i in range(1, 101):
            if i == 27 or i == 72:
                self.assertEqual("FizzBuzz", result_list[i - 1])
            elif i % 2 == 0:
                if i % 7 == 0:
                    self.assertEqual("FizzBuzz", result_list[i - 1])
                else:
                    self.assertEqual("Fizz", result_list[i - 1])
            elif i % 7 == 0:
                self.assertEqual("Buzz", result_list[i - 1])
            elif '2' in str(i):
                self.assertEqual("Fizz", result_list[i - 1])
            elif '7' in str(i):
                self.assertEqual("Buzz", result_list[i - 1])
            else:
                self.assertEqual(i, result_list[i - 1])


if __name__ == "__main__":
    # unittest.main() # 使用main()直接运行时，将按case的名称顺序执行
    suite = unittest.TestSuite()
    suite.addTest(MyTestFunc('test_3_5'))  # 将需要执行的case添加到Test Suite中，没有添加的不会被执行
    suite.addTest(MyTestFunc('test_2_7'))
    unittest.TextTestRunner().run(suite)  # 将根据case添加的先后顺序执行
