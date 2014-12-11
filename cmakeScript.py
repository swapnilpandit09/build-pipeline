import random, string
import json
from fabric.api import run, env, cd

with open('config/private.json', 'r') as fd:
	result = json.load(fd)
env.host_string = result['host']
env.password = result['password']

def randomword(length):
	return ''.join(random.choice(string.lowercase) for i in range(length))

randomName = randomword(10)

run('mkdir %s' %randomName)
with cd('%s' %randomName):
	run('git clone https://github.com/jameskbride/cmake-hello-world.git')

with cd('%s/cmake-hello-world' %randomName):
	run('mkdir build')
	with cd('build'):
		run('cmake ..')  
		run('make')
		run('./CMakeHelloWorld')
