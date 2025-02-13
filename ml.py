# import numpy as np
# import pandas as pd
# import matplotlib as plt
# import matplotlib.pyplot as plt
# import os

# ###giving path 
# # 1.{ df = pd.read_csv(r"Users/chandradhiman/Machine Learning/ML/ML_code/magic04.data")}
# #2. {df1 = pd.read_csv(r"./magic04.data")}"
# cols = ["fLength", "fwidth", "fSize", "fconc1", "fasym", "f3Long", "fM3Trans", "falpha", "fdist", "class"]
# df = pd.read_csv(r"./magic04.data", names = cols) 
# print(df.head())

# #df["class"].unique() # help to recongnize it have uniqe value
# #df["class"] = (df["class"] == "g").astype(int)  #convert g into 1

# df = pd.DataFrame(df)

# #Before conversion
# print("Before conversion:", df["class"].unique())

# # Convert "g" to 1
# df["class"] = (df["class"] == "g").astype(int)

# # After conversion
# print("After conversion:", df["class"].unique())
# print(df)

# #now give lable for every columns
# #cols = df.columns[:-1]
# cols = df.columns


# for i, label in enumerate (cols):
#    plt.hist(df[df["class"]==1][label], color = 'blue', label = label, alpha = 0.7, density=True)
#    plt.title(label)
#    plt.ylabel("Probability")
#    plt.xlabel(label)
#    plt.legend()
#    plt.show()

import numpy as np
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt
import os
# "./magic04.data"
def my_plots(filepath):

   cols = ["fLength", "fwidth", "fSize", "fconc1", "fasym", "f3Long", "fM3Trans", "falpha", "fdist", "class"]
   df = pd.read_csv(filepath, names = cols) 
   print(df.head())

   df = pd.DataFrame(df)

   #Before conversion
   print("Before conversion:", df["class"].unique())

   # Convert "g" to 1
   df["class"] = (df["class"] == "g").astype(int)

   # After conversion
   print("After conversion:", df["class"].unique())
   print(df)

   #now give lable for every columns
   #cols = df.columns[:-1]
   cols = df.columns
   print (cols)


   for i, label in enumerate (cols):
      #print (cols)
      print (i, label)
      plt.hist(df[df["class"]==1][label], color = 'blue', label = label, alpha = 0.7, density=True)
      plt.title(label)
      plt.ylabel("Probability")
      plt.xlabel(label)
      plt.legend()
      plt.show()
   return
   
my_plots("./magic04.data")