from random import randint

actions = ["ALL","SELECT","INSERT","DROP"];

def grantRoleToDatabase(numberOfDatabases, roleName):
	f = open('/Users/amishra/Scripts/output/grantRoleToDatabase.txt', 'w')
	for i in range(numberOfDatabases):
		action = getrand()
		f.write(("GRANT {} ON DATABASE db{} TO ROLE {};\n").format(action, i, roleName))
	f.close()

def getrand():
	val = randint(0, 3)
	return actions[val]

if __name__ == "__main__": 
	numberOfDatabases = 10000
	roleName = "role1"

	grantRoleToDatabase(numberOfDatabases, roleName)