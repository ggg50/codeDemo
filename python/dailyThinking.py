# daily thinking
from datetime import datetime

def writeFile(fileName, text):
  _file = open(fileName,"w+")
  _file.write(text)
  _file.close()

def genMultilineContent(tips):
  lines = []
  while True:
    line = input(tips + '(end by \'end\'): ') 
    if line == 'end': # 因为文本内容常常需要空行，这里用 end 作为本文输入结束的标识
      break
    else:
      lines.append(line)

  return '\n'.join(lines)


dStart = datetime.fromisoformat('2020-06-05T06:05:23') # 凌晨 6 点为分界
dNow = datetime.now()
days = (dNow - dStart).days

# input 
content = genMultilineContent('content')
tags = input('tags, separated by \'-\': ')
sport = input('sport: ')
title = input('title: ')
blessing = input('blessing (\'晚安\' by default): ') or '晚安'

template = """
day {days}

运动: {sport}

#{tags}#

{content}

{blessing}
"""

text = template.format(
  days = days,
  title = title, 
  sport = sport, 
  tags = tags, 
  content = content, 
  blessing = blessing, 
)

writeFile('day' + str(days) + '-' + title + '.md', text) # 创建一个文件