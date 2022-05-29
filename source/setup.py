import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'-r','requirements.txt'])
print('Installed Requirements Package!')
