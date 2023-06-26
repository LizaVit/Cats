def cats():
    cats_list = [False for i in range(0, 100)]
    cats_game = []
    for step in range(1, 101):
        for i in range(step-1, 100, step):
            cats_list[i] = not cats_list[i]
            print(step, i)
        print(list(enumerate(cats_list)))
    for i, j in enumerate(cats_list):
        if j:
            cats_game.append(i+1)       
    print(f'This cats are with hats {cats_game}')


cats()
                
#option 2

def cats():
    cats_list = list(range(1, 101))
    cats_list_game = []
    for i in cats_list:
        particular_cat = False
        for step in range(1, i+1):
            if i % step == 0:
                particular_cat = not particular_cat
        cats_list_game.append(particular_cat)
    cats_with_hats = []
    for i, j in enumerate(cats_list_game, start=1):
        if j == True:
            cats_with_hats.append(i)
    print(f'This cats are with hats {cats_with_hats}')

cats()
