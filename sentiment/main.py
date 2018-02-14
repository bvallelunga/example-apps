from encoder import Model
from decimal import Decimal

class ModelInterface():
  
  NAME = ("VG16." + __name__)
  _testData = [
    'too bad!', 
    'it was so cool, beautiful', 
    'the screenplay and the directing were horrendous', 
    'best books'
  ]
  

  def __init__(self):
    print(self.NAME, "Loading Model")
    self.model = Model()
  
  
  # Input: String
  def prediction(self, input):
    text_features = self.model.transform([ input["text"] ])
    sentiment = text_features[:, 2388][0]
    return {
      "score": Decimal(str(sentiment))
    }
    
    
if __name__ == "__main__":
  interface = ModelInterface()
  
  for text in interface._testData:
    prediction = interface.prediction({ "text": text })
    print("TEST: ", text, "\nSCORE: ", prediction["score"], "\n")
  