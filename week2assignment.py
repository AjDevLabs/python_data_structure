"""
A positive integer m can be partitioned as primes if it can be written as p + q where p > 0, q > 0 and both p and q are prime numbers.

Write a Python function primepartition(m) that takes an integer m as input and returns True if m can be partitioned as primes and False otherwise. (If m is not positive, your function should return False.)

Here are some examples of how your function should work.

>>> primepartition(7)
True

>>> primepartition(185)
False

>>> primepartition(3432)
True
"""

def is_prime(num):
     mid = num//2
     counter = 2
     while counter<=mid:
          if num%counter==0:
               return False
          counter +=1
     if counter==mid+1:
          return True
     return False

def primepartition(n):
     primes = []
     for num in range(2,n-1):
          if is_prime(num):
               primes.append(num)
     for prime in primes:
          if (n-prime) in primes:
               return True
     return False

"""
Write a function nestingdepth(s) that takes as input a string s and computes the maximum nesting depth of brackets if s has properly nested brackets. If the string is not properly matched, your function should return -1.

Hint: Use the function matched() from the practice assignment.

Here are some examples to show how your function should work.

 
>>> nestingdepth("zb%78")
0

>>> nestingdepth("(7)(a")
-1

>>> nestingdepth("a)*(?")
-1

>>> nestingdepth("((jkl)78(A)&l(8(dd(FJI:),):)?)")
4
"""
def nestingdepth(string):
     stack = []
     mdepth = 0
     depth = 0
     for c in string:
          if c=='(':
              depth +=1
              if depth>mdepth:
                   mdepth = depth
          elif c==')':
               if depth > 0:
                    depth -= 1
               else:
                    return -1
               
     if depth != 0:
          return -1
     return mdepth

"""
A list rotation consists of taking the first element and moving it to the end. For instance, if we rotate the list [1,2,3,4,5], we get [2,3,4,5,1]. If we rotate it again, we get [3,4,5,1,2].

Write a Python function rotatelist(l,k) that takes a list l and a positive integer k and returns the list l after k rotations. If k is not positive, your function should return l unchanged. Note that your function should not change l itself, and should return the rotated list.

Here are some examples to show how your function should work.

>>> rotatelist([1,2,3,4,5],1)
[2, 3, 4, 5, 1]

>>> rotatelist([1,2,3,4,5],3)
[4, 5, 1, 2, 3]

>>> rotatelist([1,2,3,4,5],12)
[3, 4, 5, 1, 2]

"""
def rotatelist(l,n):
     index = 1
     while index <= n:
          l.append(l.pop(0))
          index+=1
     return l;

print(rotatelist([1,2,3,4,5],1))
print(rotatelist([1,2,3,4,5],3))
print(rotatelist([1,2,3,4,5],12))


