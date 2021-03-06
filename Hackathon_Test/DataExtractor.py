import sys
from clarifai_basic import ClarifaiCustomModel
good = False
concept = ClarifaiCustomModel()
filename = sys.argv[1]
g = sys.argv[2]
tagArray = ['HeavyMetal','Rap', 'Alternative','Pop','Country','Classical','Electronic']
file = open('PopExcel.txt','w')
file.write('{url, genre, HeavyMetal, Rap, Alternative, Pop, Country, Classical, Electronic}\n')
with open(filename) as f:
    for line in f:
        good = False
        line = line.rstrip()        
        try:
            for genre in tagArray:
                result = concept.predict(line,genre)
                good = True    
        except:
            good = False
        if(good is True):    
            print line
            file.write('{')
            file.write(line)
            file.write(', ')
            file.write(g)
            for genre in tagArray:
                file.write(', ')
                result = concept.predict(line,genre)
                confidence = float(result['urls'][0]['score'])
                file.write(repr(confidence))
            file.write('}\n')
