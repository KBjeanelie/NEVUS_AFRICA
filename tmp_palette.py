from PIL import Image
import collections
img = Image.open(r'C:/Users/Seigneur Walter/Documents/NEVUS_AFRICA/assets/img/logo.jpeg').convert('RGB')
img = img.resize((200, 200))
pixels = list(img.getdata())
counter = collections.Counter((r // 16, g // 16, b // 16) for r, g, b in pixels)
for color, count in counter.most_common(12):
    r, g, b = [c * 16 for c in color]
    print(f'{r:03d},{g:03d},{b:03d} {count}')
