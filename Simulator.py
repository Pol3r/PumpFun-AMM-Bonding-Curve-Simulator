def smart_contract():
    
    print("****************************************")
    
    print(f"virtualTokenReserves = {virtualTokenReserves: .2f}")
    print(f"virtualSolReserves = {virtualSolReserves: .2f}")
    print("****************************************")
    print("****************************************")
def Buy():
    global pptinsol
    global amount
    global amount_
    global tokensout   
    global usdmktcap
    
    amount = float(input("SOL AMOUNT: "))
    print("****************************************")
    
    amount_ = amount * 1000000000
    tokensout = (amount_ * virtualTokenReserves) / (virtualSolReserves + amount_) / 10**6
    pptinsol = amount / tokensout
    usdmktcap = pptinsol * 1000000000 * sol
    
    if amount < 0:
        print("Invalid Input")
    else:
        return (amount_ * virtualTokenReserves) / (virtualSolReserves + amount_)

def Sell():
    global usdmktcap
    global virtualTokenReserves
    global virtualSolReserves
    global sol_out_raw
    
    amount =  float(input("TOKEN AMOUNT: "))
    print("****************************************")   
    
    if amount <=0:
        print("Invalid Input")
        return 0
    tokens_in_raw = amount * 10**6

    if tokens_in_raw > virtualTokenReserves:
        print("Insufficient Liquidity")
        return 0
    sol_out_raw = (tokens_in_raw * virtualSolReserves) / (virtualTokenReserves + tokens_in_raw)

    new_token_reserve = virtualTokenReserves + tokens_in_raw
    new_sol_reserve = virtualSolReserves - sol_out_raw
    
    price_in_sol = new_sol_reserve / new_token_reserve
    usdmktcap = price_in_sol * 10**6 * sol

    
    return tokens_in_raw 


sol = 88.03 #Change to current price of Solana if you want to simulate real-time
virtualTokenReserves = 1073000000000000
virtualSolReserves = 30000000000

Simulator = True
while Simulator == True:
    
   
    print("Smart Contract / Buy / Sell / Exit: ")
    print("1. Smart Contract")
    print("2. Buy")
    print("3. Sell")
    print("4. Exit")

    print("****************************************")
    choice = input("Enter your choice: ")
    print("****************************************")
    
    if choice == "1":
        smart_contract()        
    elif choice == "2":
        virtualTokenReserves -= Buy()        
        virtualSolReserves += amount_
        smart_contract()
        print(f"Tokens: {tokensout:,.0f}")
        print(f"MKT CAP: {usdmktcap:.0f}")
        print("****************************************")
        print("****************************************")
    elif choice == "3":
        tokens_added = Sell()
        virtualTokenReserves += tokens_added
        virtualSolReserves -= sol_out_raw
        smart_contract()
        print(f"MKT CAP: {usdmktcap:.0f}")
        print("****************************************")
        print("****************************************")
    elif choice == "4":
        break
    else:
        print("Wrong input")
