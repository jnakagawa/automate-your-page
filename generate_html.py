
def wrapper(content):
	return '''<!DOCTYPE html>
			<html>
			<title>Jonah's notes</title>''' + content + '''</html>'''

def titlegrab(text):
	titlelist=[]
	pos = 0
	start = 0
	while start != -1:
		start = text.find('TITLE', pos)
		end = text.find('\n', start)
		titlelist.append(text[start+7:end])
		pos = start + 1
	return titlelist[:-1]
def descriptiongrab(text):
	titlelist=[]
	pos = 0
	start = 0
	while start != -1:
		start = text.find('DESCRIPTION', pos)
		end = text.find('TITLE', start)
		titlelist.append(text[start+13:end])
		pos = start + 1
	return titlelist[:-1]
'''
def content_html():
'''
TEST_TEXT = """TITLE: Why Computers are Stupid
DESCRIPTION: The phrase "computers are stupid" refers 
to how they interpret instructions literally. This 
means that small typos can cause big problems.
TITLE: Python
DESCRIPTION: Python is a "programming language." It 
provides programmers a way to write instructions for a 
computer to execute in a way that the computer can understand.
TITLE: While Loops
DESCRIPTION: A while loop repeatedly executes the body of
the loop until the "test condition" is no longer true."""
print titlegrab(TEST_TEXT)
print descriptiongrab(TEST_TEXT)
def generate_divs(text):
	pos = 0
	output= ''
	for title in titlegrab(text):
		output += '''<div class="section">
				<div class ="title">''' + title + '''</div>
				<div class = "description">''' + descriptiongrab(text)[pos] +'''		</div>
				</div>'''
		pos +=1
	return output


print wrapper(generate_divs(TEST_TEXT))