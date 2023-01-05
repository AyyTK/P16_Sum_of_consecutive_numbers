"""
No one likes homework, but your math teacher has given you an assignment
to find the sum of the first N numbers. Let’s save some time by creating
a program to do the calculation for you!

Take a number N as input and output the sum of all numbers from 1 to N (including N).

Sample Input
100

Sample Output
5050

Explanation: The sum of all numbers from 1 to 100 is equal to 5050.
"""

'''version 1'''

# N = int(input("Type your number here "))
# Sum = (N / 2) * (1 + N)
# print(Sum)

'''version2'''

N = int(input())
total = 0
for i in range(N+1):
    total += i
print(total)