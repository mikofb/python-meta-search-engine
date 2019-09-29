"""
	A python search engine based on Google.
	The results can be displayed in the command prompt or in the browser.
	
	[Requires]:
				- Python3
				- yattag, it's a python module for rendering html page. It has used for the result page.
				- googlesearch: It provides many google's stuffs such as web search, image search, etc...
								It has been inclued in the Files directory.
								Just check out its README.md file for more details

	[Author]:	Mikofb at https://github.com/mikofb
	[Licence]: MIT
"""
import os
from time import gmtime, strftime
try: 
	from googlesearch import search 
except ImportError: 
	print("googlesearch module not found or not installed!") 

from yattag import Doc

"""
	yattag init...
"""
doc, tag, text = Doc().tagtext()

"""
	output variable init...
"""
results = []

def main():
	print("#-----------------------------------------#")
	print("#--------PYTHON META SEARCH ENGINE--------#")
	print("#-----------------------------------------#\n")
	query = input("$> Enter your request: ")
	"""
		Registering query to history file
	"""
	file = open("history.txt", "a")
	file.write('{0} {1}'.format(strftime("%Y-%m-%d %H:%M:%S", gmtime()), query))
	file.write('\n')
	file.close()

	answer = input("$> Display results in the browser? [y/n] ")
	print("$> Searching...")

	try:
		results = search(query, tld="co.in", num=10, stop=1, pause=2) # Check the documentation for more details
	except TimeoutError:
		print("$> [error] Please check your internet connexion!")
	
	if answer == "y":
		"""
			Generating an html output
		"""
		with tag('html', lang='fr'):
			with tag('head'):
				with tag('title'):
					text('Meta engine [Based on Google]')
				with tag('link', href='bootstrap.min.css', rel="stylesheet"):
					pass
				with tag('link', href='style.css', rel='stylesheet'):
					pass
			with tag('body'):
				with tag('div'):
					with tag('h1'):
						text('Results for : [ {} ]'.format(query))
					with tag('br'):
						pass
					with tag('p'):
						try:
							for j in results: 
								with tag('a', href='{}'.format(j)):
									text('[Link]: {}'.format(j))
								with tag('hr'):
									pass
						except:
							print("$> [error] Please check your internet connexion!")
							return
					with tag('div'):
						with tag('p'):
							text('Fin de la recherche')

		print("$> Rendering output...")
		result = doc.getvalue()
		file = open("results.html","w")
		file.write(result)
		file.close()

		print('$> Output successfully rendered!')
		print('$> Opening browser...')

		import os
		os.startfile("results.html")
	elif answer =="n":
		try:
			print('Results for : [ {} ]'.format(query))
			for j in results:
				print(j)
		except:
			print("$> [error] Please check your internet connexion!")
			return

#-----------------------------------------------
#					  MAIN
#-----------------------------------------------
if __name__ == '__main__':
	main()

