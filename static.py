commerce_buildings = '便利店 五金店 服装店 菜市场 学校 图书城 商贸中心 加油站 民食斋 媒体之声'.split()
residence_buildings = '木屋 居民楼 钢结构房 平房 小型公寓 人才公寓 花园洋房 中式小楼 空中别墅 复兴公馆'.split()
industry_buildings = '木材厂 食品厂 造纸厂 水厂 电厂 钢铁厂 纺织厂 零件厂 企鹅机械 人民石油'.split()
default_blacklist = "商贸中心 小型公寓 水厂 花园洋房 复兴公馆 加油站 人民石油 纺织厂 钢结构房 钢铁厂 菜市场".split()
modes = ["online", "offline", "train"]
buffs_100 = {
                '木屋': ['木材厂'],
                '居民楼': ['便利店'],
                '钢结构房': ['钢铁厂'],
                '花园洋房': ['商贸中心'],
                '空中别墅': ['民食斋'],

                '便利店': ['居民楼'],
                '五金店': ['零件厂'],
                '服装店': ['纺织厂'],
                '菜市场': ['食品厂'],
                '学校':  ['图书城'],
                '图书城': ['学校', '造纸厂'],
                '商贸中心': ['花园洋房'],
                '民食斋': ['空中别墅'],

                '木材厂': ['木屋'],
                '食品厂': ['菜市场'],
                '造纸厂': ['图书城'],
                '钢铁厂': ['钢结构房'],
                '纺织厂': ['服装店'],
                '零件厂': ['五金店'],
                '企鹅机械': ['零件厂'],
                '人民石油': ['加油站']
}

buffs_50 = {'零件厂': ['企鹅机械'],
            '加油站': ['人民石油']
            }

bufflist_258 = tuple([.2, .5, .8, 1.1, 1.4])
bufflist_246 = tuple([.2, .4, .6, .8, 1.0])
bufflist_015 = tuple([0.75*x for x in [.2, .4, .6, .8, 1.0]])
bufflist_010 = tuple([0.5*x for x in [.2, .4, .6, .8, 1.0]])
bufflist_005 = tuple([0.25*x for x in [.2, .4, .6, .8, 1.0]])
bufflist_035 = tuple([1.75*x for x in [.2, .4, .6, .8, 1.0]])

buffs_ind = {
             '媒体之声': bufflist_005,
             '钢铁厂': bufflist_015,
             '中式小楼': bufflist_246,
             '民食斋': bufflist_246,
             '空中别墅': bufflist_246,
             '电厂': bufflist_258,
             '企鹅机械': bufflist_010,
             '人才公寓': bufflist_035
             }

buffs_bus = {
             '媒体之声': bufflist_005,
             '企鹅机械': bufflist_010,
             '民食斋': bufflist_246,
             '纺织厂': bufflist_015,
             '人才公寓': bufflist_246,
             '中式小楼': bufflist_246,
             '空中别墅': bufflist_246,
             '电厂': bufflist_258
             }

buffs_res = {
             '媒体之声': bufflist_005,
             '企鹅机械':bufflist_010,
             '民食斋': bufflist_246,
             '人才公寓': bufflist_246,
             '平房': bufflist_246,
             '空中别墅': bufflist_246,
             '电厂': bufflist_258,
             '中式小楼': bufflist_035
             }

UnitDict = {
        'G': 1,
        'K': 1e3,
        'M': 1e6,
        'B': 1e9,
        'T': 1e12,
        'aa': 1e15,
        'bb': 1e18,
        'cc': 1e21,
        'dd': 1e24,
        'ee': 1e27,
        'ff': 1e30,
        'gg': 1e33,
        'hh': 1e36,
        'ii': 1e39
}
