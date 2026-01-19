import os
import sys
import traceback

# Setup environment to match FlaskFarm
sys.path.append('/Volumes/WD/Users/Work/python/flaskfarm/lib')
sys.path.append('/Volumes/WD/Users/Work/python/ff_dev_plugins/support_site')

try:
    from support import SupportSC
    print("SupportSC imported successfully")
    
    current_dir = '/Volumes/WD/Users/Work/python/ff_dev_plugins/support_site'
    init_file = os.path.join(current_dir, '__init__.py')
    
    print(f"Loading wavve from {current_dir}")
    try:
        mod = SupportSC.load_module_f(init_file, 'wavve')
        print(f"Module loaded: {mod}")
        if mod:
            print(f"Attributes: {dir(mod)}")
            if hasattr(mod, 'SupportWavve'):
                print("SupportWavve found!")
            else:
                print("SupportWavve NOT found in module")
    except Exception as e:
        print(f"Execution Error: {e}")
        traceback.print_exc()

except Exception as e:
    print(f"Import Error: {e}")
    traceback.print_exc()
