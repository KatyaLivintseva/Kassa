while True:
    print(' ')
    try:
        N=int(input('Введите сумму и нажмите Enter '))
        if N<0:
            print('Введите положительное число')
            continue
        S=N

        a1=1 # достоинства купюр
        a2=2
        a4=4
        a8=8
        a16=16
        a32=32
        a64=64

        col64=0 # количество купюр
        col32=0
        col16=0
        col8=0
        col4=0
        col2=0
        col1=0

        while N!=0: # пока сумма не станет равной 0, т.е пока её не выплатят полностью
            if N>=a64:
                N=N-a64
                col64=col64+1
            
            else:
                if N>=a32:
                    N=N-a32
                    col32=col32+1
                    
                else:
                    if N>=a16:
                        N=N-a16
                        col16=col16+1
                    
                    else:
                        if N>=a8:
                            N=N-a8
                            col8=col8+1
                        
                        else:
                            if N>=a4:
                                N=N-a4
                                col4=col4+1
                                                
                            else:
                                if N>=a2:
                                    N=N-a2
                                    col2=col2+1
                                
                                else:
                                    if N>=a1:
                                        N=N-a1
                                        col1=col1+1

        print('Сумму',S,'можно выплатить следующими купюрами:')
        print(' ')
        print('Номинал    Количество')
        if col64>0:
            print(a64,'       ',col64)
        if col32>0:
            print(a32,'       ',col32)
        if col16>0:    
            print(a16,'       ',col16)
        if col8>0:    
            print(a8,'        ',col8)
        if col4>0:    
            print(a4,'        ',col4)
        if col2>0:    
            print(a2,'        ',col2)
        if col1>0:    
            print(a1,'        ',col1)     

    except ValueError:
        print('Введите целое, положительное число')                         