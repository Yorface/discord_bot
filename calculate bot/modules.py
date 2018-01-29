import math

class Microphage_decomposition:
    def __init__(self, number):
        self.number=number

    def calculate(self):
        d=2
        f=open('소인수분해.txt', 'w')
        while self.number>=d:
            if self.number%d==0:
                self.number=self.number/d
                f.write(str(d))
                f.write(' ')
            else:
                d+=1
        f.close()
        f = open("소인수분해.txt", 'r')
        output = f.read()
        f.close()
        return output

class reduction_of_a_fraction:
    def __init__(self, number1, number2):
        self.number1=number1
        self.number2=number2

    def calculate(self):
        d=2
        while self.number1>=d or self.number2>=d:
            if self.number1%d==0:
                if self.number2%d==0:
                    self.number1=self.number1/d
                    self.number2=self.number2/d
            else:
                d+=1
        if self.number1<0 or self.number2<0:
            if self.number1<0 and self.number2<0:
                self.number1=-self.number1
                self.number2=-self.number2
            if self.number1>=0 and self.number2<0:
                self.number2=-self.number2
                self.number1=-self.number1
        output='%s/%s'%(int(self.number1),int(self.number2))
        return output

class simultaneous_equations:
    def __init__(self, ax1, by1, c1, ax2, by2, c2):
        self.ax1=ax1
        self.by1=by1
        self.c1=-c1
        self.ax2=ax2
        self.by2=by2
        self.c2=-c2

    def calculate(self):
        ad=self.ax1*self.ax2
        bd=self.by1*self.ax2
        cd=self.c1*self.ax2
        ae=self.by2*self.ax1
        af=self.c2*self.ax1
        try:
            (cd-af)/(bd-ae)
        except ZeroDivisionError:
            output='0으로 나눌수 없습니다'
            return output
        else:
            y=(cd-af)/(bd-ae)
            cc=cd-af
            x=(self.c1-self.by1*y)/self.ax1
            output='x=%f ,y=%f'%(x,y)
            return output

class a_quadratic_equation:
    def __init__(self,aqustn,bqustn,cqustn):
        self.aqustn=aqustn
        self.bqustn=bqustn
        self.cqustn=-cqustn

    def calculate(self):
        if self.aqustn==0:
            output='이차방정식이 아닙니다'
            return output
        D=self.bqustn**2-4*self.aqustn*self.cqustn
        if D>0:
            x1=(-self.bqustn+ math.sqrt(D))/(2*self.aqustn)
            x2=(-self.bqustn- math.sqrt(D))//(2*self.aqustn)
            output='해는: %s, %s'%(x1,x2)
            return output
        elif D==0:
            X=(-self.bqustn/(2*self.aqustn))
            output='해는: %s'%X
            return output
        else:
            output='해가 없습니다'
            return output
