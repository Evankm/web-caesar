def encrypt(plainText, shift): 
  newtext = ""
  abc ='abcdefghijklmnopqrstuvwxyz'
  ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  for i in plainText:
    if i in abc:
      stayInAlphabet = abc.index(i) + shift 
      while stayInAlphabet >= len(abc):
        stayInAlphabet -= 26
      lastletter = abc[stayInAlphabet]
      newtext += lastletter
    elif i in ABC:
        stayInAlphabet = ABC.index(i) + shift 
        while stayInAlphabet >= len(ABC):
          stayInAlphabet -= 26
        lastletter = ABC[stayInAlphabet]
        newtext += lastletter

    else:
       i.isalpha()== False
       newtext += i
  print(newtext)
  return newtext

encrypt('PYthon', 2)