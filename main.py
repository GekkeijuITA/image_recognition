#IMPORT
from PIL import Image
import numpy as np

#FUNCTION


#MAIN
i = Image.open("images/dot.png")
iar = np.asarray(i)

print(iar)