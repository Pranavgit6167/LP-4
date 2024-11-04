class Fibonacci():
    def fibo_non(self,n):
        result=[]
        num1=0
        num2=1
        
        for i in range(n):
            result.append(num1)
            num1,num2=num2,num1+num2
        print(result)
        
    def fibo_recu(self,n,memo={}):
        if n<=1:
            return n
        if n not in memo:
             memo[n]=obj.fibo_recu(n-1,memo)+obj.fibo_recu(n-2,memo)
        
        return memo[n]
        
n=int(input("Enter Number:\t"))  
obj=Fibonacci()
print(obj.fibo_non(n))
for i in range(n):
    print(obj.fibo_recu(i))