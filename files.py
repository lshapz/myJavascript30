import os
import string

for root, dirs, files in os.walk('.'):
    for fname in files:
        if fname.endswith('ED.html') or fname.endswith('ED.js'):
            os.remove(os.path.join(root, fname))
# removes FINISHED files -aka the answers

# for fileName in os.listdir("."):
#   if fileName[0].isdigit():
#     os.rename(fileName, fileName.replace(" ", ""))
# # removes whitespace from folders 