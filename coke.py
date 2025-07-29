price=50
valid_coins={5,10,25}

while price > 0:
    print(f"Amount Due: {price}")
    insert=int(input("Insert Coin"))
    if insert in  valid_coins:
        result=abs(price-insert)
        print(f"Change Owed: {result}")
        price -= insert
        if result == 0:
            break
    else:
        continue

input()