def cats():
    cats_list = [False for i in range(0, 10)]
    cats_game = []
    for step in range(1, 11):
        for i in range(step-1, 10, step):
            cats_list[i] = not cats_list[i]
            print(step, i)
        print(list(enumerate(cats_list)))
    for i, j in enumerate(cats_list):
        if j:
            cats_game.append(i+1)       
    print(f'This cats are with hats {cats_game}')


cats()
                

#test
