# pairwise-player-trade

## 领域

游戏、图形与多媒体

## 主题

玩家交易

## 说明

改动重置确认、服务端锁定与断线回滚。

初始状态下 `gameplay/player_trade.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
