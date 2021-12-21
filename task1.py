while True:
    

    try:  
        
        a = int(input("Enter any  Integer : "))
                        
    except ValueError as ae:
        
        print(a)
        print(" You entered an invalid integer !!!" , ae)
    
