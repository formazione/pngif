from PIL import Image, ImageDraw, ImageFont
# from IPython.display import display, HTML
import os


color = "yellow"
def create_text(size, text):
    global color
    img = Image.new('RGB', (700, 200), "black")
    draw = ImageDraw.Draw(img)
    draw.text((size[0], size[1]+10), text, font = fnt, fill=color)
    return img

iromeo = Image.open("romeo.png")
ibenvolio = Image.open("benvolio.png")

def image(image, size, text):
    global color, over40, fcount
    if stuck == "romeo":
      color = "blue"
    elif stuck == "benvolio":
      color = "darkred"
    else:
      color = "darkgreen"
    img = Image.new('RGB', (700, 200), "yellow")

    img2 = Image.open(image)
    img.paste(img2,(30,25))
    draw = ImageDraw.Draw(img)
    draw.text((size[0]+50, size[1]+10), text, font = fnt, fill=color)
    draw.text((int(fcount/5), 180), ">" , font = fnt, fill=color)
    return img

def text_pause(img,text):
  # If first character is empty the pause is twice
  global fcount
  pause = 10
  if len(text) > 0:
    if text[0] == " " and len(text) > 2: 
      pause = 30 * text[:3].count(" ")
  for i in range(pause):
    new_frame = image(img, [30,0], text)
    fcount += 1
    frames.append(new_frame)
# Create the frames
frames = []
stuck = ""
fcount = 0
def roll(text, *actors):
    global stuck, fcount

    if text[2:6] == "Rom.":
      stuck = "romeo"
    elif text == "BENVOLIO...":
      stuck = "benvolio"
    else:
      if stuck == "romeo":
        for i in range(len(text)+1):
            new_frame = image("romeo.png", [30,0], text[:i])
            fcount += 1
            frames.append(new_frame)
        text_pause("romeo.png", text)
      elif stuck == "benvolio":
        for i in range(len(text)+1):
            new_frame = image("benvolio.png",[300,0], text[:i])
            fcount += 1
            frames.append(new_frame)
        text_pause("benvolio.png", text)
      else:
          for i in range(len(text)+1):
            new_frame = create_text([0,10], text[:i])
            frames.append(new_frame)
            fcount += 1
          for n in range(5): # This makes the text stand at the end for a sec
            new_frame = create_text([0,10], text)
            fcount += 1
            frames.append(new_frame)


    
fnt = ImageFont.truetype("arial", 24)

# a space before the text means a pause, 2 or 3 spaces a longer one

TXT = """
Scene II.
Capulet's orchard.

Enter Romeo.


  Rom. He jests at scars that never felt a wound.

                     Enter Juliet above at a window.

    But soft! What light through yonder window breaks?
    It is the East, and Juliet is the sun!
    Arise, fair sun, and kill the envious moon,
    Who is already sick and pale with grief
    That thou her maid art far more fair than she.
    Be not her maid, since she is envious.
    Her vestal livery is but sick and green,
    And none but fools do wear it. Cast it off.
    It is my lady; O, it is my love!
    O that she knew she were!
    She speaks, yet she says nothing. What of that?
    Her eye discourses; I will answer it.
    I am too bold; 'tis not to me she speaks.
    Two of the fairest stars in all the heaven,
    Having some business, do entreat her eyes
    To twinkle in their spheres till they return.
    What if her eyes were there, they in her head?
    The brightness of her cheek would shame those stars
    As daylight doth a lamp; her eyes in heaven
    Would through the airy region stream so bright
    That birds would sing and think it were not night.
    See how she leans her cheek upon her hand!
    O that I were a glove upon that hand,
    That I might touch that cheek!

""".splitlines()
# text is a line of all text and it is passed to roll2
for text in TXT:
  roll(text)

print(f"Numero di frame: {fcount}")
# Save into a GIF file that loops forever
frames[0].save('cartoon16.gif', format='GIF',
               append_images=frames[1:], save_all=True, duration=45, loop=0)
os.startfile("cartoon16.gif")