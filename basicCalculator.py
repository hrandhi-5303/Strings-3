class Solution:
    def calculate(self,s):
        s=s.replace(' ', '')
        stack=[]
        num=0
        sign ='+'
        n=len(s)

        for i,ch in enumerate(s):
            if ch.isdigit():
                num=num*10+int(ch)
                
            if (not ch.isdigit() and ch !=' ')  or i == n-1:
                if sign =='+':
                    stack.append(num)
                elif sign =='-':
                    stack.append(-num)
                elif sign =='*':
                    prev = stack.pop()
                    stack.append(prev * num)
                else: #sign =='/':
                    prev = stack.pop()
                    stack.append(int(prev / num))

                sign =ch
                num=0
        
        return sum(stack)
    
if __name__=='__main__':
    sol=Solution()
    print(sol.calculate("3+2*2"))
    print(sol.calculate(" 3/2 "))
    print(sol.calculate("3+5 / 2"))