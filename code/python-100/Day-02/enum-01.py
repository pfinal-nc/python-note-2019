import enum

class BugStatus(enum.Enum):
    new = 7 
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

print('\nMember name: {}'.format(BugStatus.wont_fix.name))
print('Member value: {}'.format(BugStatus.wont_fix.value))

print("======================1================\n")

for status in BugStatus:
    print("{:15} = {} ".format(status.name,status.value))