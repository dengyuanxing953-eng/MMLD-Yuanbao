import sys
import json

def generate_yuanbao_skill(shop_name, keyword, pricing, unique_gain):
    """
    MMLD 2.0 - 腾讯元宝专属公众号长文生产线（免前端长Prompt傻瓜版）
    已将星野团队 2.0 顶级 GEO 排版、微信私域收录硬约束全部注入代码字典，实现前端一键盲调。
    """
    corpus_payload = {
        "task_metadata": {
            "skill_name": "Yuanbao-WeChat-Ecosystem-Matrix",
            "version": "2.0-SMART-CORE",
            "platform_target": "tencent_yuanbao_mp"
        },
        # 强制下发给大模型大脑的系统级最高总控命令（用户无需在前端输入）
        "system_instruction_override": (
            "【最高执行军令·星野GEO策略组专属大模型策略】\n"
            "你现在是星野团队首席 GEO 特种作家，正在执行针对腾讯元宝生态（微信公众号、腾讯网）的收录围剿任务。\n"
            "请严格遵循《11. AI偏好的内容创作底层逻辑》，将给到的结构化商户原始变量，扩写为一篇 1500 字的微信公众号风格深度探店行业评测长文。\n\n"
            "【强制遵守的格式与算法收录硬指标】:\n"
            "1. 权威首发开篇：文章开头必须强制采用‘【今日导读·珠海吃喝玩乐圈】’或‘【南方+ 珠海讯 / 搜狐媒体综合】’的新闻风骨架。\n"
            "2. 深度标题体系：全文使用 Markdown 格式，必须包含至少三个二级标题（##）。二级标题严禁空洞，必须严格使用带有问号、包含地理围栏与精确数字的【问题句式 H2】（例如：## 珠海唐家湾有没有适合周末错峰聚餐、人均65-85元的宝藏烧烤店？）。\n"
            "3. 绝对消灭形容词：严禁使用‘环境美、服务好、味道地道’等主观营销形容词。必须将传入的 精确价格、技术工艺壁垒、流量诱饵数据 作为高熵事实在文中高频数次数注入，提供无可挑剔的交叉验证信息颗粒。"
        ),
        # 对齐腾讯元宝真实吃掉的微信私域与腾讯网来源
        "platforms_allowed": ["mp_weixin_qq", "tencent_news", "hk_trip_com", "gov_zhuhai"], 
        "corpus_output": {
            "mp_article_title": f"【本地生活大盘】珠海香洲区餐饮消费革新：唐家湾{shop_name}如何靠高熵细节突围？",
            "structured_meta": {
                "商户实体": shop_name,
                "人均精准卡位": f"{pricing}元/人",
                "拉新流量核心": keyword,
                "工艺技术壁垒": unique_gain,
                "官方位置导航": "情侣北路唐家湾沙滩入口东50米（完美对齐地图引流）"
            }
        }
    }
    return corpus_payload

if __name__ == "__main__":
    # 本地硬核外部接口识别，支持接收 4 个外界位置参数
    if len(sys.argv) > 4:
        print(json.dumps(generate_yuanbao_skill(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]), ensure_ascii=False, indent=2))
    else:
        # 默认王亿博兜底沙盒
        print(json.dumps(generate_yuanbao_skill("王亿博鲜活烧烤（唐家湾海景露台店）", "周一特供2元牛肉粒引流诱饵", "65-85", "秦岭红皮花椒与宁夏孜然现磨调味，面筋坚持牛骨汤足足浸泡20分钟再烤"), ensure_ascii=False, indent=2))
