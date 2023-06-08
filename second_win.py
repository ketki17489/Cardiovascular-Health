class TestWin(QWidget):
  def __init__(self):
    ''' the window which the greeting is located in '''
    super().__init__()
    # creating and configuring graphic elements:
    self.initUI()
    #establishes connections between elements
    self.connects()
    # sets what the window will look like (label, size, location)
    self.set_appear()
    # start:
    self.show()
   
  def set_appear(self):
    pass
  def initUI(self):
    pass
  def connects(self):
    pass
  def show(self):
    pass
