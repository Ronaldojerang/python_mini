def play_flames(count, flame):
    while len(flame) > 1:
        index = (count % len(flame)) - 1

        if index >= 0:
            flame = flame[index+1:] + flame[:index]
        else:
            flame = flame[:len(flame)-1]

    return flame[0]


if __name__ == "__main__":
    p1 = input("name2: ")
    p2 = input("nam1: ")
    
    ls = []
    val = []

    print(p1)
    print(p2)

    count = 0
    run = 0
    
    for i in p1:
        if i in ls:
            continue
        ls.append(i)
        
        for j in p1:
            if i == j:
                count = count + 1 
        
        for j in p2:
            if i == j:
               count = count - 1
        val.append(count)
        count = 0 

    for i in p2:
        if i in ls:
            continue
        ls.append(i)
        for j in p2:
            if i == j:
                count = count + 1 
        val.append(count)       
        count = 0

    for i in val:
        
        if i < 0:
            #val.pop(i)
            
            run += - i
            continue
    for i in val:
        if i >= 0:
            count += i
    #count = sum([i for i in val if i >= 0]) + run
    print(count)
    flame = ["Friends", "Lovers", "Affectionate", "Marriage", "Enemies", "Siblings"]
    
    result = play_flames(count, flame)

    print("The relationship between", p1, "and", p2, "is:", result)
