# ROS-less Xacro
Forked from [ros/xacro](https://github.com/ros/xacro), this branch allows the xacro converters to be run _without_ the ROS environment.

## Use

```bash
cd .../xacro
python xacro.py .../path/to/file.xacro > .../path/to/output.urdf --inorder

# If there are failures, try adding the "oldorder" flag
python xacro.py .../path/to/file.xacro > .../path/to/output.urdf --oldorder
```

## Changes

- Moved `xacro` folder to the root so it's easier to run.
- Add a custom `resolve_args` function to so the ROS one does not have to be used.
