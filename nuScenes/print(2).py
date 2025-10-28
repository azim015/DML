from nuscenes.nuscenes import NuScenes
from nuscenes.utils.data_classes import LidarPointCloud
from nuscenes.map_expansion.map_api import NuScenesMap
import matplotlib.pyplot as plt

print(2)

nusc = NuScenes(version='v1.0-mini', dataroot='/data/nuscenes', verbose=True)

print(f"Scenes: {len(nusc.scene)} | Samples: {len(nusc.sample)} | Annotations: {len(nusc.sample_annotation)}")

scene = nusc.scene[0]
sample = nusc.get('sample', scene['first_sample_token'])
print("Sensors:", sample['data'].keys())

# === Visualization (old SDK compatible) ===
nusc.render_sample(sample['token'])                 # renders all camera views
nusc.render_sample_data(sample['data']['CAM_FRONT'])  # renders one camera

# === LIDAR exploration ===
lidar_data = nusc.get('sample_data', sample['data']['LIDAR_TOP'])
lidar_path = f"{nusc.dataroot}/{lidar_data['filename']}"
pc = LidarPointCloud.from_file(lidar_path)

plt.figure(figsize=(7,7))
plt.scatter(pc.points[0, :], pc.points[1, :], s=0.01)
plt.xlabel("X [m]")
plt.ylabel("Y [m]")
plt.title("LIDAR Top View")
plt.axis("equal")
plt.show()

# === Map info ===
nusc_map = NuScenesMap(dataroot='/data/nuscenes', map_name='boston-seaport')
print(f"Map layers: {len(nusc_map.lane)} lanes | {len(nusc_map.drivable_area)} drivable areas")