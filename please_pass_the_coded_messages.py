'''
Please Pass the Coded Messages
==============================

You need to pass a message to the bunny workers, but to avoid detection, the code you agreed to use is... obscure, to say the least.
The bunnies are given food on standard-issue plates that are stamped with the numbers 0-9 for easier sorting, and you need to combine
sets of plates to create the numbers in the code. The signal that a number is part of the code is that it is divisible by 3.
You can do smaller numbers like 15 and 45 easily, but bigger numbers like 144 and 414 are a little trickier.
Write a program to help yourself quickly create large numbers for use in the code, given a limited number of plates to work with.

You have L, a list containing some digits (0 to 9). Write a function solution(L) which finds the largest number that can be made
from some or all of these digits and is divisible by 3. If it is not possible to make such a number, return 0 as the solution.

L will contain anywhere from 1 to 9 digits.  The same digit may appear multiple times in the list, but each element in the list may only be used once.

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

Input:
solution.solution([3, 1, 4, 1])
Output:
    4311

Input:
solution.solution([3, 1, 4, 1, 5, 9])
Output:
    94311
'''

from itertools import permutations

def solution(l):
    code = ''
    l.sort(reverse = True)
    if sum(l) % 3 == 0:
        return "".join(map(str, l))
    list_len = len(l)
    while list_len != 0:
        for i in list(permutations(l, list_len)):
            if sum(i) % 3 == 0:
                code += "".join(map(str, i))
                return "".join(map(str, i))
        list_len -=1
    return "0"

print(solution([-1]))