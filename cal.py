import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.font_manager import FontProperties

# 設定中文字型 (指定系統中的支援字型)
font_path = "NotoSansCJK-Regular.ttc"  # 替換成您的字型路徑
font_prop = FontProperties(fname=font_path)
rcParams['font.family'] = font_prop.get_name()

# 設定標題與說明
st.title("健保看診次數損益平衡分析")
st.write("動態調整參數，查看健保點數與損益平衡所需看診次數的對應關係。")

# 輸入參數
overtime_fee = st.sidebar.number_input("時薪 (每小時)", value=320)
transport_fee = st.sidebar.number_input("交通費 (單次)", value=50)
registration_fee = st.sidebar.number_input("掛號費 (單次)", value=150)

# 固定參數
monthly_health_fee = 895  # 每月健保費
annual_health_fee = monthly_health_fee * 12  # 年健保費

# 計算損益平衡看診次數
points_range = np.arange(500, 1001, 10)  # 健保點數範圍 (500 - 1000, 每次增加10點)
breakeven_visits = []

for points_per_visit in points_range:
    total_expenses_per_visit = overtime_fee + transport_fee + registration_fee
    if 0.9 * points_per_visit > total_expenses_per_visit:  # 確保分母為正
        breakeven_x = (annual_health_fee) / (0.9 * points_per_visit - total_expenses_per_visit)
        breakeven_visits.append(breakeven_x)
    else:
        breakeven_visits.append(float('inf'))  # 無法損益平衡


# 繪製圖表
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(points_range, breakeven_visits, label="損益平衡看診次數", color="b")
ax.set_title("健保點數與損益平衡看診次數", fontsize=14)
ax.set_xlabel("健保點數 (每次看診)", fontsize=12)
ax.set_ylabel("損益平衡所需看診次數", fontsize=12)
ax.grid(alpha=0.5)
ax.legend()

# 在左邊顯示圖表
st.pyplot(fig)

# 在右側顯示表格
st.write("### 每年所需看診次數")
# 計算損益平衡看診次數
points_range = np.arange(500, 2001, 100)  # 健保點數範圍 (500 - 1000, 每次增加10點)
breakeven_visits = []

for points_per_visit in points_range:
    total_expenses_per_visit = overtime_fee + transport_fee + registration_fee
    if 0.9 * points_per_visit > total_expenses_per_visit:  # 確保分母為正
        breakeven_x = (annual_health_fee) / (0.9 * points_per_visit - total_expenses_per_visit)
        breakeven_visits.append(round(breakeven_x, 0))
    else:
        breakeven_visits.append('無法回本')  # 無法損益平衡
# 數據框
df = pd.DataFrame({
    "健保點數": points_range,
    "所需看診次數": breakeven_visits
})
st.dataframe(df)
