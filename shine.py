from matplotlib import pyplot as plt
from colour import Color
import numpy as np
import time


plt.figure(figsize=(10, 6))

start_color = Color("red")
end_color = Color("green")


colors = list(start_color.range_to(end_color, 50))

tmp = {}
for i in range(len(colors)):
    tmp[i] = list(colors[i].range_to(Color("blue"), 50))

arr = []
print(range(len(colors)))

for i in range(len(colors)-1):
    tmp_list = []
    
    for o in tmp:
        print(f"{o = } {i = } {len(tmp) = } {len(tmp[o]) = }")
        tmp_list.append(tmp[o][i].rgb)
    
    arr.append(tmp_list)



for i, data in enumerate(arr):
    data = np.expand_dims(data, axis=0)

    if i == 1:
        time.sleep(10)
        
    # Отображаем данные
    plt.imshow(data)
    plt.pause(0.1) # задержки между кадрами
    plt.clf() # для очистки текущего изображения
