import sys
from clarifai_basic import ClarifaiCustomModel
concept = ClarifaiCustomModel()
url = sys.argv[1]
max = 0
prediction = ''
tagArray = ['HeavyMetal','Rap', 'Alternative','Pop','Country','Classical','Electronic']
for genre in tagArray:
    #print genre
    result = concept.predict(url,genre)
    confidence = float(result['urls'][0]['score'])
    #if confidence > max:
        #max = confidence
        #prediction = genre
    print genre, 'Confidence rate: ', confidence
#print prediction
