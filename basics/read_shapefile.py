import geopandas as gpd

shp_path = "example.shp"  # 先占位

gdf = gpd.read_file(shp_path)
print(gdf.head())
print("CRS:", gdf.crs)
