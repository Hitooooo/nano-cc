# Nano Claude Code

## 快速开始

### 环境要求
- Python >= 3.11
- uv（Python包管理工具）

### 安装步骤

1. 克隆项目
```bash
git clone <repository-url>
cd nano-cc
```

2. 配置环境变量
```bash
cp .env.example .env
# 编辑 .env 文件，填入你的 API 密钥
```

3. 安装依赖
```bash
uv sync
```

### 运行项目

```bash
# 激活虚拟环境
source .venv/bin/activate  # macOS/Linux
# 或
.venv\Scripts\activate  # Windows

# 运行主程序
python agent.py
```

### 依赖说明
- `anthropic` - Anthropic API 客户端
- `python-dotenv` - 环境变量管理
- `pyyaml` - YAML 配置文件解析
