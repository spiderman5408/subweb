#全局变量定义
subip = 'https://hh.clash008.top'      # 默认subip是 subconverter 后台端口，在config/perf.ini 中指定，或者docker的端口指定。
apiip = 'https://qq.clash008.top'      #apiip 是 suweb 前端端口
passwd = '17733906174a.'                      #passwd 是 admin系统的密码
#proxygroup  用于节点分组，当您修改pref.ini的 [ruleset] 需要改变以下默认值以一一对应，否则会导致节点分组报错。
proxygroup= '@🔰 节点选择`select{groupname}[]DIRECT'\
            '@📲 电报吹水`select`[]🔰 节点选择{groupname}[]DIRECT'\
            '@📹 YouTube`select`[]🔰 节点选择{groupname}[]DIRECT'\
            '@🎥 NETFLIX`select`[]🔰 节点选择{groupname}[]DIRECT'\
            '@📺 巴哈姆特`select`[]🔰 节点选择{groupname}[]DIRECT'\
            '@🌍 国外媒体`select`[]🔰 节点选择{groupname}[]DIRECT'\
            '@Ⓜ️ 微软服务`select`[]DIRECT`[]🔰 节点选择{groupname}'\
            '@🍎 苹果服务`select`[]DIRECT`[]🔰 节点选择{groupname}'\
            '@🛑 全球拦截`select`[]REJECT`[]DIRECT'\
            '@🐟 漏网之鱼`select`[]🔰 节点选择`[]DIRECT{groupname}'
