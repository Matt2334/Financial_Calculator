# Future Value = PV * (1+r)^n
def FV():
    pv = int(input("Enter Present Value: "))
    r = int(input("Enter Interest rate per period: "))/100
    n = int(input("Enter the number of periods: "))
    return round(pv * (1+r)**n,2)

# Present Value = FV/(1+r)^n
def PV():
    fv = int(input("Enter Future Value: "))
    r = int(input("Enter Interest rate per period: "))/100
    n = int(input("Enter the number of periods: "))
    return round(fv / (1+r)**n, 2)

# Net Present Value = sum (Ct/(1+r)^t)-C0
def npv():
    # might need to fix, requires testing
    C0 = int(input("What is your initial investment? "))
    r = int(input("What is your discount rate? "))/100
    t = int(input("How many time periods? "))
    sum = 0
    for i in range(1, t+1):
        Ct = int(input(f"What is the cash flow at period {i}? "))
        sum+= Ct/((1+r)**t)
    return round(sum-C0,2)

# Internal Rate of Return (IRR) -> 0 = sum (Ct / (1+IRR)**t ) - C0
def internal_rate_of_return():
    pass

# Annuity Payments = (pv * r)/(1-(1+r)**-n)
def annuity():
    pv = input("Enter present Value: ")
    r = input("Enter Interest rate per period: ")
    n = input("Enter the number of periods: ")
    return (pv * r)/(1- (1+r)**n )


# Loan Amortization -> PMT = ((P*r) * (1+r)**n) / (1+r)**n -1
def load_amortization():
    pass

# Compound Interest -> A = P * (1+r/n)**(n*t)
def compound_interest():
    pass

# Simple Interest -> I = P * r * t
def simple_interest():
    pass

# Dividend Discount Model (DDM) -> P0 = D1/(r-g)

def main():
    print(npv())






if __name__=="__main__":
    main()
