#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np


number = np.random.randint(1,101)    # загадали число


def game_core_v3(number):
    '''Функция с минимальными попытками угадывания чисел'''
    
    count = 1 # счетчик попыток
    '''В переменных low и high границы угадываемого числа'''
    low = 1
    high = 101
    predict = high//2 # сужаем границы
    
    while number != predict: # пока эта часте не будет ровна
        count+=1
        
        if number > predict: 
            low = predict + 1
        
        elif number < predict: 
            high= predict - 1
        predict = (low+high)//2 # проверяем средний элимент

    return(count) # выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")

    return(score)


score_game(game_core_v3)


# In[ ]:




