
import json

newPrefix = "new_"
oldEntryOrder = ["title", "description", "tags"]

def convertEntry(entry):
	newEntry = {}
	for [i, key] in enumerate(oldEntryOrder):
		newEntry[key] = entry[i]
	return newEntry

def convertJson(fileName):
	with open(fileName, "r") as f:
		# Load the contents of the file into a variable
		data = json.load(f)

	newData = {}
	newData["common"] = []
	for key in data.keys():
		if key != "common":
			newData[key] = data[key]
			continue
		else:
			for entry in data[key]:
				# print(convertEntry(entry))
				newEntry = convertEntry(entry)
				newData[key].append(newEntry)



	with open(newPrefix+fileName, "w") as f:
    # Write the data to the file
		json.dump(newData, f, indent=4)

def testJson(fileName):
	with open(fileName, "r") as f:
		# Load the contents of the file into a variable
		data = json.load(f)

	print(data[0])

if __name__ == "__main__":
	# convertJson("vscode.json")
	# convertJson("vim.json")
	testJson("index.json")

