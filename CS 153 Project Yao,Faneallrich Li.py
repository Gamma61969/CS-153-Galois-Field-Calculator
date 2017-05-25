from functools import reduce

def setGF2(degree, irPoly):
    global mask1, mask2, polyred
    mask1 = mask2 = 1 << degree
    mask2 -= 1
    polyred = reduce(lambda x, y: (x << 1) + y, irPoly[1:])    
         
def mul(p1, p2):
    p = 0
    while p2:
        if p2 & 1:
            p ^= p1
        p1 <<= 1
        if p1 & mask1:
            p1 ^= polyred
        p2 >>= 1
    return p & mask2

def Mul2(p1, p2):
    return mul(p2I(p1), p2I(p2))

def i2P(sInt):
    return [(sInt >> i) & 1 for i in reversed(range(sInt.bit_length()))]
 
def p2I(ldPoly):
    return reduce(lambda x, y: (x << 1) + y, ldPoly)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def mulinv(b, n):
    g, x, q = egcd(b, n)
    if g == 1:
        return x % n

class Polynomial:
    def __init__(self,coefficient):
        self.cf = coefficient
    def add(self,x):
        if len(self.cf)>len(x.cf):
            res = self.cf
            for w in range(len(x.cf)):
               res[w] = (res[w] ^  x.cf[w])
               print str(res[w])+ " xor " + str(x.cf[w])
        else:
            res = x.cf
            for w in range(len(self.cf)):
                res[w] = (res[w] ^ self.cf[w])
                print str(res[w])+ " xor " + str(x.cf[w])
        return Polynomial(res)
    
    
x = raw_input("Input the first polynomial A(x)")
y = raw_input("Input the second polynomial. B(x)")
z = raw_input("Input the Irreducible Polynomial R(x)")

pol1 = []
pol2 = []
pol3 = []

for i in x.split(" "):
    q = int(i)
    pol1.append(q)

for i in y.split(" "):
    q = int(i)
    pol2.append(q)


for i in z.split(" "):
    q = int(i)
    pol3.append(q)
print pol1
print pol2

pol1.reverse()
pol2.reverse()

w = Polynomial(pol1)
ww = Polynomial(pol2)
www = Polynomial(pol3)
ip = raw_input("Enter the Operation \n(a)A(x) + B(x) \n(b)A(x) - B(x)\n(c)A(x)B(x) \n(d)A(x)/B(x)\nThe program will exit after each process\n")
if(ip == "a" or ip == "A"):
    e =  w.add(ww).cf
    e.reverse()
    print e
elif(ip == "b" or ip == "B"):
    e =  w.add(ww).cf
    e.reverse()
    print e
elif(ip == "c" or ip == "C"):
    pol1.reverse()
    print p2I(pol1)
    pol2.reverse()
    print p2I(pol2)
    print p2I(pol3)
    degree = len(pol3) - 1
    setGF2(degree, pol3)
    print i2P(Mul2(pol1,pol2))
    
elif(ip == "d" or ip == "D"):
    degree = len(pol3) - 1
    setGF2(degree, pol3)
    a = p2I(pol1)
    b = p2I(pol2)
    c = p2I(pol3)
    d = mulinv(b,c)
    e = mul(a,d)
    f = i2P(e)
    print f
