#Gear Calculator
def Gear():
  #variable definitions
  ratio = 1/float(input("Your desired gear ratio is:"))
  minDifUser = float(input("What is the biggest desired difference from your ratio? "))
  minTeeth = int(input("How many teeth does the smallest gear possible have? "))
  maxTeeth = int(input("How many teeth does the biggest gear possible have? "))
  maxGears = int(input("How many gears can you use? (100 max) "))
  
  flipped = False
  
  #user input checking
  if ratio > 1:
    ratio = 1/ratio
    flipped = True
  
  if maxGears <= 1 or maxGears > 100:
    maxGears = 4
    print("Max gears was set to 4")
      
  if (maxGears % 2) == 1:
    maxGears -= 1
    print("Max gears was set to", maxGears)
  
  
  fractions = [1]
  values = ["useless"]
  curr = []
  poss = 1
  minDif = 10000
  currValue = []
  minIndex = []
  finalRatio = 1.0
  
  for i in range(int(maxGears/2)):
    curr.append(0)
  
  for n in range(minTeeth,maxTeeth):
    for d in range(n+1, maxTeeth+1):
      a = (n/d)
      if not a in fractions:
        fractions.append(a)
        values.append([n,d])
  
  while curr[0] < len(fractions):
    for i in curr:
      poss = poss * fractions[i]
  
    if (abs(ratio - poss)) <= minDifUser:
      minIndex = curr + ["Don't worry about it"]
      del minIndex[-1]
      print("Found it!")
      break
    elif (abs(ratio - poss)) < minDif:
      minDif = abs(ratio - poss)
      minIndex = curr + ["Don't worry about it"]
      del minIndex[-1]
      #if flipped:
       # print("New best:", poss)
      #else:
       # print("New best:", 1/poss)
    
    poss = 1
    
    #Adding
    x = len(curr) - 1
    y = 0
    curr[x] += 1
    while curr[x] == len(fractions):
      if x == 0:
        break
      x -= 1
      curr[x] += 1
      y += 1
      for i in range(1,y+1):
        curr[x+i] = curr[(x+i-1)]
    
    
    
  if flipped:
    minIndex.reverse()
  
  for index in minIndex:
    if not index == 0:
      if flipped:
        currValue.append(list(reversed(values[index])))
      else:
        currValue.append(values[index])
    
  for i in currValue:
    finalRatio = finalRatio * (i[0]/i[1])
  
  print("\nThe best ratio found is %s and was found using %d gears." % (str(1/finalRatio),len(currValue) * 2))
  print("The gears are as follow:")
  
  for i in range(1, len(currValue)+1):
    j = currValue[i-1]
    print("Gear %d connected to axle %d has %d teeth." % (i * 2 - 1, (i // 2) + 1, j[0]))
    print("Gear %d connected to axle %d has %d teeth." % (i * 2, (i // 2) + 2, j[1]))
