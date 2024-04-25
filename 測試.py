import numpy as np
a = np.zeros((15,15))
for i in range(-7,8):
    for k in range(-7,8):
        a[i+7][k+7] = abs(i)+13*abs(k)
np.save("C:/Users/morga/Desktop/程式/音樂資料/計算.npy", a)
