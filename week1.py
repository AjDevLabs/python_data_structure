def matched(string):
     depth = 0
     o=False
     for c in string:
          if c=='(':
               depth += 1
               o=True
          elif c==')' and o:
               depth -= 1
     if not depth:
          return True
     return False


def intreverse(n):
     rev = 0 
     while n>0:
          rev = rev*10+(n%10)
          n = n // 10
     return rev

def isPrime(n):
     if n<2:
          return False
     mid = (n//2)+1
     for x in range(2,mid):
          if not n%x:
               return False
     return True

def sumprimes(l):
     s=0
     for n in l:
          if isPrime(n):
               s += n
     return s

print(sumprimes([3,3,1,13]))
print(sumprimes([2,4,6,9,11]))
print(sumprimes([-3,1,6]))

"""
print(matched("zb%78"))
print(matched("(7)(a"))
print(matched("a)*(?"))
print(matched("((jkl)78(A)&l(8(dd(FJI:),):)?)"))
"""
print(matched("a3qw3;4w3(aasdgsd)((agadsgdsgag)agaga)"))
print(matched("(ag(Gaga(agag)Gaga)GG)a)33)cc("))
print(matched("(adsgdsg(agaga)a"))
print(matched("15ababa.agaga[][[["))

